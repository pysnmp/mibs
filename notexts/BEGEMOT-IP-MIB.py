#
# PySNMP MIB module BEGEMOT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-IP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:26:31 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ObjectIdentity, Counter64, MibIdentifier, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Integer32, IpAddress, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ObjectIdentity", "Counter64", "MibIdentifier", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3))
if mibBuilder.loadTexts: begemotIp.setLastUpdated('200602130000Z')
if mibBuilder.loadTexts: begemotIp.setOrganization('German Aerospace Center')
begemotIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
mibBuilder.exportSymbols("BEGEMOT-IP-MIB", begemotIpObjects=begemotIpObjects, PYSNMP_MODULE_ID=begemotIp, begemotIp=begemotIp)
