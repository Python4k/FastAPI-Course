from sqlalchemy import insert, select
from app.database.models import async_session

class BaseController:
    model = None
    
    @classmethod
    async def get_all(cls):
        """
        Retrieves all records from the database table associated with the
        model defined in the controller.

        Returns:
            A list of all records in the database table associated with the model.
        """
        async with async_session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def get_all_by_filter(cls, **kwargs):
        """
        Retrieves records from the database table associated with the
        model defined in the controller based on the given keyword arguments.

        Args:
            **kwargs: Keyword arguments specifying the values to filter the records by.

        Returns:
            A list of records that match the given keyword arguments.
        """
        async with async_session() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def get_by_id(cls, id):
        """
        Retrieves a record from the database table associated with the
        model defined in the controller based on the given id.

        Args:
            id (int): The id of the record to retrieve.

        Returns:
            The record with the given id, or None if no record is found.
        """
        async with async_session() as session:
            query = select(cls.model).where(cls.model.id == id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

        
    @classmethod
    async def get_one_or_none(cls, **kwargs):
        """
        Retrieves a record from the database table associated with the
        model defined in the controller based on the given keyword arguments.

        Args:
            **kwargs: Keyword arguments specifying the values to filter the records by.

        Returns:
            The record that matches the given keyword arguments, or None if no record is found.
        """
        async with async_session() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def add(cls, **kwargs):
        """
        Inserts a new record into the database table associated with the
        model defined in the controller based on the given keyword arguments.

        Args:
            **kwargs: Keyword arguments specifying the values to insert into the record.

        Returns:
            The newly inserted record.
        """
        async with async_session() as session:
            query = insert(cls.model).values(**kwargs)
            await session.execute(query)
            await session.commit()

