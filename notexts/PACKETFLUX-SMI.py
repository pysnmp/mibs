#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.8 at Mon Jan 17 18:30:57 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, Counter32, Bits, Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, enterprises, Counter64, IpAddress, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "enterprises", "Counter64", "IpAddress", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
packetflux = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050))
packetflux.setRevisions(('2013-06-04 16:31', '2013-06-04 21:58',))
if mibBuilder.loadTexts: packetflux.setLastUpdated('201306041631Z')
if mibBuilder.loadTexts: packetflux.setOrganization('PacketFlux Technologies')
packetfluxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 1))
if mibBuilder.loadTexts: packetfluxProducts.setStatus('current')
packetfluxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 2))
if mibBuilder.loadTexts: packetfluxMgmt.setStatus('current')
mibBuilder.exportSymbols("PACKETFLUX-SMI", packetflux=packetflux, PYSNMP_MODULE_ID=packetflux, packetfluxProducts=packetfluxProducts, packetfluxMgmt=packetfluxMgmt)
