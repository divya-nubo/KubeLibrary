
    def get_cronjobs_in_namespace(self, name_pattern, namespace, label_selector=""):
        """Gets cronjobs matching pattern in given namespace.
        Can be optionally filtered by label. e.g. label_selector=label_key=label_value
        Returns list of cronjobs.
        - ``name_pattern``:
          cronjobs name pattern to check
        - ``namespace``:
          Namespace to check
        """
        ret = self.v1.list_namespaced_cronjobs(namespace, watch=False, label_selector=label_selector)
        r = re.compile(name_pattern)
        cronjobs = [item for item in ret.items if r.match(item.metadata.name)]
        return cronjobs	
