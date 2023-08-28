import bpy


class KeymapperProperties(bpy.types.PropertyGroup):

    operator_categories = []
    cat_list = dir(bpy.ops)

    for i in cat_list:
        operator_categories.append((i, i.capitalize(), ''))

    current_category = ''

    def update_cat(self, context):
        self.current_category = self.category

    def get_operators(self, context):
        operator_list = []
        op_cat = eval(f'bpy.ops.{context.scene.keymapper_props.category}')
        op_list = dir(op_cat)

        for i in op_list:
            operator_list.append((i, i.capitalize(), ''))

        return operator_list

    def search_op(self, context):
        context.space_data.filter_type = 'NAME'
        context.space_data.filter_text = f'{self.operator} {self.category}'

    category: bpy.props.EnumProperty(
        name='Category',  # noqa: F821
        description='List of Categories',
        items=operator_categories,
        update=update_cat,
    )

    operator: bpy.props.EnumProperty(
        name='Operator',  # noqa: F821
        description='List of Operators',
        items=get_operators,
        update=search_op,
    )
