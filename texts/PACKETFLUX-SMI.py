#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.8 at Tue Sep 12 13:01:45 2023
# On host fv-az575-466 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Bits, NotificationType, Unsigned32, Gauge32, ModuleIdentity, Integer32, ObjectIdentity, iso, Counter64, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "ObjectIdentity", "iso", "Counter64", "enterprises", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PACKETFLUX-SMI", packetfluxProducts=packetfluxProducts, PYSNMP_MODULE_ID=packetflux, packetfluxMgmt=packetfluxMgmt, packetflux=packetflux)
