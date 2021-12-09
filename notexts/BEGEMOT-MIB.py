#
# PySNMP MIB module BEGEMOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB
# Produced by pysmi-1.1.3 at Thu Dec  9 15:20:10 2021
# On host fv-az83-649 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
fokus, = mibBuilder.importSymbols("FOKUS-MIB", "fokus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, Counter32, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, MibIdentifier, Gauge32, NotificationType, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "Counter32", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "MibIdentifier", "Gauge32", "NotificationType", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemot = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1))
if mibBuilder.loadTexts: begemot.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: begemot.setOrganization('Fraunhofer FOKUS, CATS')
mibBuilder.exportSymbols("BEGEMOT-MIB", begemot=begemot, PYSNMP_MODULE_ID=begemot)
