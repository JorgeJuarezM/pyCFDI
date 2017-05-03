import SOAPpy
import base64
from suds.client import Client
from subprocess import call
from lxml import etree



comprobante = etree.Element("{http://www.sat.gob.mx/cfd/3}Comprobante", nsmap={
	'cfdi': 'http://www.sat.gob.mx/cfd/3',
	'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
})


comprobante.set("{http://www.w3.org/2001/XMLSchema-instance}schemaLocation", "http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd")
comprobante.set("lugarExpedicion", "COLIMA,COL. MEXICO")
comprobante.set("moneda", "PESOS")
comprobante.set("tipoCambio", "1")
comprobante.set("certificado", "MIIEYTCCA0mgAwIBA...")
comprobante.set("folio", "1")
comprobante.set("formaDePago", "PAGO EN UNA SOLA EXHIBICION")
comprobante.set("metodoDePago", "NO IDENTIFICADO")


emisor = etree.SubElement(comprobante, "{http://www.sat.gob.mx/cfd/3}Emisor")
emisor.set("nombre", "ASOCIACION DE AGRICULTORES DEL DISTRITO DE RIEGO 004 DN MARTIN")


print(etree.tostring(comprobante, pretty_print=True, xml_declaration=True, encoding="UTF-8"))



# document = etree.Element('Comprobante', nsmap={'a': 'http://a.b/c'})
# node = etree.SubElement(document, 'inner')
# node.set("cosa-rara", "valor")
# print(etree.tostring(document, xml_declaration=True, encoding='UTF-8'))

# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = tostring(elem, "UTF-8")
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="  ")


# top = Element('Comprobante')
# top.set("lugarExpedicion", "Colima Colima")
# top.set("moneda", "MXN")

# emisor = SubElement(top,"Emisor")

# print prettify(top)


# top.set("version", "1.0")
# comment = Comment('Generated for PyMOTW')
# top.append(comment)

# child = SubElement(top, 'child')
# child.text = 'This child contains text.'

# child_with_tail = SubElement(top, 'child_with_tail')
# child_with_tail.text = 'This child has regular text.'
# child_with_tail.tail = 'And "tail" text.'

# child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
# child_with_entity_ref.text = 'This & that'

# print tostring(top)


# et = ElementTree(top)

# f = BytesIO()
# et.write(f, encoding='utf-8', xml_declaration=True) 
# print(f.getvalue())  # your XML file, encoded as UTF-8


# openssl pkcs8 -inform DET -outform PEM -in key.key -passin pass:12345678a -out key.pem
# call(["openssl","pkcs8", "-inform", "DET", "-outform", "PEM", "-in", "key.key", "-passin", "pass:12345678a", "-out", "key2.pem"])




# # Read the xml file and encode it on base64
# invoice_path = "factura.xml"
# file = open(invoice_path)
# lines = "".join(file.readlines())
# xml = base64.encodestring(lines)


# url = "http://demo-facturacion.finkok.com/servicios/soap/stamp.wsdl"
# client = Client(url,cache=None)

# username = "contacto@jorgejuarez.net"
# password = "j0rg3CFDI$"

# contenido = client.service.stamp(xml,username,password)

# print contenido

