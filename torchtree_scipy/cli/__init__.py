from torchtree.cli.plugin import Plugin


class SciPy(Plugin):
    def load_arguments(self, subparsers):
        for name, parser in subparsers._name_parser_map.items():
            parser.add_argument(
                '--scipy_gamma_site',
                action="store_true",
                help="""use the GammaSiteModel implemented with SciPy""",
            )

    def process_tree_likelihood(self, arg, json_tree_likelihood):
        if (
            arg.scipy_gamma_site
            and isinstance(json_tree_likelihood, dict)
            and isinstance(json_tree_likelihood['site_model'], dict)
        ):
            json_tree_likelihood['site_model'][
                'type'
            ] = 'torchtree_scipy.GammaSiteModel'
