class CodeElement:
    indent_size = 2

    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}def __init__(self):')

        if self.name:
            i1 = ''
            lines.append(f'')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.lines = [f'class {root_name}:', f'  def __init__(self):']

    def add_field(self, type, name):
        self.lines.append(f'    self.{type} = {name}')
        return self

    def __str__(self):
        return '\n'.join(self.lines)


if __name__ == '__main__':
    cb = CodeBuilder('Person')\
            .add_field('name', '""')\
            .add_field('age', '0')

    print(cb)