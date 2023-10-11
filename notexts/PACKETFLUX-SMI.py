#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.8 at Wed Oct 11 08:00:25 2023
# On host fv-az622-326 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, enterprises, TimeTicks, Counter64, ObjectIdentity, ModuleIdentity, Bits, Integer32, MibIdentifier, NotificationType, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "enterprises", "TimeTicks", "Counter64", "ObjectIdentity", "ModuleIdentity", "Bits", "Integer32", "MibIdentifier", "NotificationType", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
packetflux = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050))
packetflux.setRevisions(('2013-06-04 16:31', '2013-06-04 21:58',))
if mibBuilder.loadTexts: packetflux.setLastUpdated('201306041631Z')
if mibBuilder.loadTexts: packetflux.setOrganization('PacketFlux Technologies')
packetfluxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 1))
if mibBuilder.loadTexts: packetfluxProducts.setStatus('current')
packetfluxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 2))
if mibBuilder.loadTexts: packetfluxMgmt.setStatus('current')
mibBuilder.exportSymbols("PACKETFLUX-SMI", packetflux=packetflux, packetfluxMgmt=packetfluxMgmt, packetfluxProducts=packetfluxProducts, PYSNMP_MODULE_ID=packetflux)
