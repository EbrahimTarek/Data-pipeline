from Base import session
from tables import PprRawAll, PprCleanAll

from sqlalchemy import cast, Integer, Date
from sqlalchemy.dialects.postgresql import insert


def insert_transactions():
    """
    Insert operation: add new data
    """
    # Retrieve all the transaction ids from the clean table
    clean_transaction_ids = session.query(PprCleanAll.transaction_id)

    # date_of_sale and price needs to be casted as their
    # datatype is not string but, respectively, Date and Integer
    transactions_to_insert = session.query(
        cast(PprRawAll.date_of_sale, Date),PprRawAll.address,PprRawAll.postal_code,PprRawAll.county,
        cast(PprRawAll.price, Integer),
        PprRawAll.description,).filter(~PprRawAll.transaction_id.in_(clean_transaction_ids))
	
    # Print total number of transactions to insert
    print("Transactions to insert:", transactions_to_insert.count())
    
    # Insert the rows from the previously selected transactions
    stm = insert(PprCleanAll).from_select(
        ["date_of_sale", "address", "postal_code", "county", "price", "description"],
        transactions_to_insert,)

    # Execute and commit the statement to make changes in the database.
    session.execute(stm)
    session.commit()


def delete_transactions():
    """
    Delete operation: delete any row not present in the last snapshot
    """
    # Get all ppr_raw_all transaction ids
    raw_transaction_ids = session.query(PprRawAll.transaction_id)

    # Filter all the ppt_clean_all table transactions that are not present in the ppr_raw_all table
    # and delete them.
    # Passing synchronize_session as argument for the delete method.
    transactions_to_delete = session.query(PprCleanAll).filter(
        ~PprCleanAll.transaction_id.in_(raw_transaction_ids))
    
    # Print transactions to delete
    print("Transactions to delete:", transactions_to_delete.count())

    # Delete transactions
    transactions_to_delete.delete(synchronize_session=False)

    # Commit the session to make the changes in the database
    session.commit()

def main():
    print("[Load] Start")
    print("[Load] Inserting new rows")
    insert_transactions()
    print("[Load] Deleting rows not available in the new transformed data")
    delete_transactions()
    print("[Load] End")

