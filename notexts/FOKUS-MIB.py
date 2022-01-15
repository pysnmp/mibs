#
# PySNMP MIB module FOKUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FOKUS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:26:11 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, NotificationType, ObjectIdentity, IpAddress, iso, ModuleIdentity, enterprises, Integer32, TimeTicks, Counter32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "iso", "ModuleIdentity", "enterprises", "Integer32", "TimeTicks", "Counter32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fokus = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325))
if mibBuilder.loadTexts: fokus.setLastUpdated('200202050000Z')
if mibBuilder.loadTexts: fokus.setOrganization('Fraunhofer FOKUS, CATS')
mibBuilder.exportSymbols("FOKUS-MIB", fokus=fokus, PYSNMP_MODULE_ID=fokus)
