#
# PySNMP MIB module BEGEMOT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-IP-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 11:13:02 2023
# On host fv-az590-991 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, iso, Integer32, Counter32, Bits, ModuleIdentity, Unsigned32, NotificationType, TimeTicks, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "iso", "Integer32", "Counter32", "Bits", "ModuleIdentity", "Unsigned32", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemotIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3))
if mibBuilder.loadTexts: begemotIp.setLastUpdated('200602130000Z')
if mibBuilder.loadTexts: begemotIp.setOrganization('German Aerospace Center')
begemotIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
mibBuilder.exportSymbols("BEGEMOT-IP-MIB", begemotIpObjects=begemotIpObjects, begemotIp=begemotIp, PYSNMP_MODULE_ID=begemotIp)
