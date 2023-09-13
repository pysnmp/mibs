#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.8 at Wed Sep 13 08:06:35 2023
# On host fv-az370-447 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, enterprises, Integer32, NotificationType, iso, Unsigned32, Bits, MibIdentifier, IpAddress, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "enterprises", "Integer32", "NotificationType", "iso", "Unsigned32", "Bits", "MibIdentifier", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
packetflux = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050))
packetflux.setRevisions(('2013-06-04 16:31', '2013-06-04 21:58',))
if mibBuilder.loadTexts: packetflux.setLastUpdated('201306041631Z')
if mibBuilder.loadTexts: packetflux.setOrganization('PacketFlux Technologies')
packetfluxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 1))
if mibBuilder.loadTexts: packetfluxProducts.setStatus('current')
packetfluxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 2))
if mibBuilder.loadTexts: packetfluxMgmt.setStatus('current')
mibBuilder.exportSymbols("PACKETFLUX-SMI", packetflux=packetflux, packetfluxMgmt=packetfluxMgmt, PYSNMP_MODULE_ID=packetflux, packetfluxProducts=packetfluxProducts)
