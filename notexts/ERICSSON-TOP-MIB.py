#
# PySNMP MIB module ERICSSON-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TOP-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:02:21 2024
# On host fv-az1433-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Bits, NotificationType, IpAddress, enterprises, TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity, iso, Counter64, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Bits", "NotificationType", "IpAddress", "enterprises", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "iso", "Counter64", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericsson = ModuleIdentity((1, 3, 6, 1, 4, 1, 193))
ericsson.setRevisions(('2008-10-17 00:00', '2002-05-28 00:00',))
if mibBuilder.loadTexts: ericsson.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericsson.setOrganization('Ericsson AB ')
ericssonModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 183))
if mibBuilder.loadTexts: ericssonModules.setStatus('current')
mibBuilder.exportSymbols("ERICSSON-TOP-MIB", PYSNMP_MODULE_ID=ericsson, ericssonModules=ericssonModules, ericsson=ericsson)
