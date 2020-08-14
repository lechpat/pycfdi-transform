import xml.sax


class TSaxBase:

    def __init__(self):
        super().__init__()

    def parse_file(self, handler, xml_file):
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(xml_file)


