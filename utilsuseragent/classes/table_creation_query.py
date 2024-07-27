TABLE_CREATION_QUERY = '''
                        CREATE TABLE user_agent (
                            user_agent TEXT PRIMARY KEY NOT NULL UNIQUE,
                            browser_family TEXT,
                            browser_major INTEGER,
                            browser_minor INTEGER,
                            browser_patch INTEGER,
                            os_family TEXT,
                            os_major INTEGER,
                            os_minor INTEGER,
                            os_patch INTEGER,
                            os_patch_minor INTEGER,
                            device_family TEXT,
                            device_brand TEXT,
                            device_model TEXT
                        )
                    '''