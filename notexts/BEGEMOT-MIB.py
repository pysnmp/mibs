#
# PySNMP MIB module BEGEMOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:02:05 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
fokus, = mibBuilder.importSymbols("FOKUS-MIB", "fokus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Bits, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, NotificationType, MibIdentifier, Integer32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Bits", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemot = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1))
if mibBuilder.loadTexts: begemot.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: begemot.setOrganization('Fraunhofer FOKUS, CATS')
mibBuilder.exportSymbols("BEGEMOT-MIB", PYSNMP_MODULE_ID=begemot, begemot=begemot)
