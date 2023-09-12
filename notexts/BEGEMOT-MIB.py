#
# PySNMP MIB module BEGEMOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 12:20:56 2023
# On host fv-az615-431 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
fokus, = mibBuilder.importSymbols("FOKUS-MIB", "fokus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ModuleIdentity, iso, NotificationType, ObjectIdentity, Integer32, MibIdentifier, Unsigned32, Gauge32, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ModuleIdentity", "iso", "NotificationType", "ObjectIdentity", "Integer32", "MibIdentifier", "Unsigned32", "Gauge32", "Counter64", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemot = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1))
if mibBuilder.loadTexts: begemot.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: begemot.setOrganization('Fraunhofer FOKUS, CATS')
mibBuilder.exportSymbols("BEGEMOT-MIB", begemot=begemot, PYSNMP_MODULE_ID=begemot)
