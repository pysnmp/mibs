#
# PySNMP MIB module BEGEMOT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-IP-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 09:31:40 2023
# On host fv-az581-610 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, iso, IpAddress, Bits, NotificationType, MibIdentifier, Integer32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "iso", "IpAddress", "Bits", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3))
if mibBuilder.loadTexts: begemotIp.setLastUpdated('200602130000Z')
if mibBuilder.loadTexts: begemotIp.setOrganization('German Aerospace Center')
begemotIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
mibBuilder.exportSymbols("BEGEMOT-IP-MIB", begemotIp=begemotIp, begemotIpObjects=begemotIpObjects, PYSNMP_MODULE_ID=begemotIp)
