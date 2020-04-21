def sample_query(self):
    # Sample Query
    query = "SELECT first_name, last_name FROM {TBL_USR} WHERE " \
            "last_name LIKE 'M%';".format(TBL_USR=USERS)
    self.print_all_data(query=query)
    # Sample Query Joining
    query = "SELECT u.last_name as last_name, " \
            "a.email as email, a.address as address " \
            "FROM {TBL_USR} AS u " \
            "LEFT JOIN {TBL_ADDR} as a " \
            "WHERE u.id=a.user_id AND u.last_name LIKE 'M%';" \
        .format(TBL_USR=USERS, TBL_ADDR=ADDRESSES)
    self.print_all_data(query=query)


def sample_delete(self):
    # Delete Data by Id
    query = "DELETE FROM {} WHERE id=3".format(USERS)
    self.execute_query(query)
    self.print_all_data(USERS)
    # Delete All Data
    '''
    query = "DELETE FROM {}".format(USERS)
    self.execute_query(query)
    self.print_all_data(USERS)
    '''


def sample_insert(self):
    # Insert Data
    query = "INSERT INTO {}(id, first_name, last_name) " \
            "VALUES (3, 'Terrence','Jordan');".format(USERS)
    self.execute_query(query)
    self.print_all_data(USERS)


def sample_update(self):
    # Update Data
    query = "UPDATE {} set first_name='XXXX' WHERE id={id}" \
        .format(USERS, id=3)
    self.execute_query(query)
    self.print_all_data(USERS)

