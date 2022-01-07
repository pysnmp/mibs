#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.8 at Fri Jan  7 16:15:33 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Gauge32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, iso, enterprises, Unsigned32, Bits, TimeTicks, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "iso", "enterprises", "Unsigned32", "Bits", "TimeTicks", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
packetflux = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050))
packetflux.setRevisions(('2013-06-04 16:31', '2013-06-04 21:58',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: packetflux.setRevisionsDescriptions(('initial version of this module', 'Correct MIB ID',))
if mibBuilder.loadTexts: packetflux.setLastUpdated('201306041631Z')
if mibBuilder.loadTexts: packetflux.setOrganization('PacketFlux Technologies')
if mibBuilder.loadTexts: packetflux.setContactInfo('custsvc@packetflux.com    \n                            http://www.packetflux.com')
if mibBuilder.loadTexts: packetflux.setDescription('SMI MIB for PacketFlux Technologies')
packetfluxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 1))
if mibBuilder.loadTexts: packetfluxProducts.setStatus('current')
if mibBuilder.loadTexts: packetfluxProducts.setDescription('packetfluxProducts is the root OBJECT IDENTIFIER\n                            for products released by packetflux technologies.')
packetfluxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 2))
if mibBuilder.loadTexts: packetfluxMgmt.setStatus('current')
if mibBuilder.loadTexts: packetfluxMgmt.setDescription('This is the main subtree for all packetflux product\n                            management mibs.')
mibBuilder.exportSymbols("PACKETFLUX-SMI", packetflux=packetflux, packetfluxProducts=packetfluxProducts, PYSNMP_MODULE_ID=packetflux, packetfluxMgmt=packetfluxMgmt)
