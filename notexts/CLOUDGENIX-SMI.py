#
# PySNMP MIB module CLOUDGENIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source CLOUDGENIX-SMI
# Source digest sha256:30654b9792d171a448ede49f041d997d21a068fd419b81cc6eb1d4facd11c173
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cloudgenix = ModuleIdentity((1, 3, 6, 1, 4, 1, 50114))
cloudgenix.setRevisions(('2017-06-19 18:00',))
if mibBuilder.loadTexts: cloudgenix.setLastUpdated('2022-02-24 19:35')
if mibBuilder.loadTexts: cloudgenix.setOrganization('Palo Alto Networks, Inc.')
class CgxDegreesC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class CgxVolts(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

cgxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 1))
cgxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2))
cgxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 1))
cloudgenixCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 50114, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cloudgenixCompliance = cloudgenixCompliance.setStatus('current')
cgxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 2))
cgxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 10))
if mibBuilder.loadTexts: cgxMgmt.setStatus('current')
cgxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 11))
if mibBuilder.loadTexts: cgxProducts.setStatus('current')
mibBuilder.exportSymbols("CLOUDGENIX-SMI", CgxDegreesC=CgxDegreesC, CgxVolts=CgxVolts, PYSNMP_MODULE_ID=cloudgenix, cgxCompliances=cgxCompliances, cgxConformance=cgxConformance, cgxGroups=cgxGroups, cgxMgmt=cgxMgmt, cgxObjects=cgxObjects, cgxProducts=cgxProducts, cloudgenix=cloudgenix, cloudgenixCompliance=cloudgenixCompliance)
