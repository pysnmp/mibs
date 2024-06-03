#
# PySNMP MIB module ERICSSON-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TOP-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:38:58 2024
# On host fv-az1210-277 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Counter32, ModuleIdentity, ObjectIdentity, NotificationType, enterprises, IpAddress, MibIdentifier, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Counter32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "enterprises", "IpAddress", "MibIdentifier", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ericsson = ModuleIdentity((1, 3, 6, 1, 4, 1, 193))
ericsson.setRevisions(('2008-10-17 00:00', '2002-05-28 00:00',))
if mibBuilder.loadTexts: ericsson.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericsson.setOrganization('Ericsson AB ')
ericssonModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 183))
if mibBuilder.loadTexts: ericssonModules.setStatus('current')
mibBuilder.exportSymbols("ERICSSON-TOP-MIB", PYSNMP_MODULE_ID=ericsson, ericssonModules=ericssonModules, ericsson=ericsson)
