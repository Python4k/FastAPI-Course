from datetime import date
from app.database.models import engine, async_session 
from sqlalchemy import and_, func, insert, or_, select
from app.database.controller import BaseController
from app.bookings.models import Booking
from app.hotels.models import Room

class BookingController(BaseController):
    model = Booking
    
    @classmethod
    async def add(
        cls,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
    ):
        """
        WITH booked_rooms AS (
            SELECT * FROM bookings
            WHERE room_id = 1 AND
                (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
                (date_from <= '2023-05-15' AND date_to > '2023-05-15')
        )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """
        try:
            async with async_session() as session:
                booked_rooms = (
                    select(Booking)
                    .where(
                        and_(
                            Booking.room_id == room_id,
                            or_(
                                and_(
                                    Booking.date_from >= date_from,
                                    Booking.date_from <= date_to,
                                ),
                                and_(
                                    Booking.date_from <= date_from,
                                    Booking.date_to > date_from,
                                ),
                            ),
                        )
                    )
                    .cte("booked_rooms")
                )

                """
                SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
                LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
                WHERE rooms.id = 1
                GROUP BY rooms.quantity, booked_rooms.room_id
                """

                get_rooms_left = (
                    select(
                        (Room.quantity - func.count(booked_rooms.c.room_id)).label(
                            "rooms_left"
                        )
                    )
                    .select_from(Room)
                    .join(booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True)
                    .where(Room.id == room_id)
                    .group_by(Room.quantity, booked_rooms.c.room_id)
                )

                # Рекомендую выводить SQL запрос в консоль для сверки
                # print(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))

                Room_left = await session.execute(get_rooms_left)
                Room_left: int = Room_left.scalar()


                if Room_left > 0:
                    get_price = select(Room.price).filter_by(id=room_id)
                    price = await session.execute(get_price)
                    price: int = price.scalar()
                    add_booking = (
                        insert(Booking)
                        .values(
                            room_id=room_id,
                            user_id=user_id,
                            date_from=date_from,
                            date_to=date_to,
                            price=price,
                        )
                        .returning(
                            Booking.id, 
                            Booking.user_id, 
                            Booking.room_id,
                            Booking.date_from,
                            Booking.date_to,
                        )
                    )

                    new_booking = await session.execute(add_booking)
                    await session.commit()
                    return new_booking.mappings().one()
                else: 
                    return None

        except Exception as e:
            print(e)
            
    
                