#
# PySNMP MIB module BEGEMOT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-IP-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 12:39:40 2024
# On host fv-az658-333 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, NotificationType, Bits, MibIdentifier, Counter32, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "NotificationType", "Bits", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemotIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3))
if mibBuilder.loadTexts: begemotIp.setLastUpdated('200602130000Z')
if mibBuilder.loadTexts: begemotIp.setOrganization('German Aerospace Center')
begemotIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
mibBuilder.exportSymbols("BEGEMOT-IP-MIB", begemotIpObjects=begemotIpObjects, PYSNMP_MODULE_ID=begemotIp, begemotIp=begemotIp)
