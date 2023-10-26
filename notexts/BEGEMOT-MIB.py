#
# PySNMP MIB module BEGEMOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 10:07:31 2023
# On host fv-az351-613 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
fokus, = mibBuilder.importSymbols("FOKUS-MIB", "fokus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, Bits, Integer32, IpAddress, iso, MibIdentifier, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "Bits", "Integer32", "IpAddress", "iso", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemot = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1))
if mibBuilder.loadTexts: begemot.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: begemot.setOrganization('Fraunhofer FOKUS, CATS')
mibBuilder.exportSymbols("BEGEMOT-MIB", begemot=begemot, PYSNMP_MODULE_ID=begemot)
