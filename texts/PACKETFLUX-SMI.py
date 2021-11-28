#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.3 at Sun Nov 28 20:08:59 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, TimeTicks, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, enterprises, Counter64, MibIdentifier, NotificationType, Gauge32, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "enterprises", "Counter64", "MibIdentifier", "NotificationType", "Gauge32", "IpAddress", "Counter32")
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
mibBuilder.exportSymbols("PACKETFLUX-SMI", PYSNMP_MODULE_ID=packetflux, packetflux=packetflux, packetfluxMgmt=packetfluxMgmt, packetfluxProducts=packetfluxProducts)
