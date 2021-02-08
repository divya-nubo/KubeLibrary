    def get_secrets(self, label_selector=""):
        """Gets a list of available namespaces.
        Can be optionally filtered by label. e.g. label_selector=label_key=label_value
        Returns list of namespaces.
        """
        ret = self.v1.list_secret_for_all_namespaces(watch=False, label_selector=label_selector)
        return [item.metadata.name for item in ret.items]	
		
