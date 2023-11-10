#
# PySNMP MIB module ERICSSON-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TOP-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:45:06 2023
# On host fv-az447-590 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ModuleIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Integer32, TimeTicks, MibIdentifier, NotificationType, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "TimeTicks", "MibIdentifier", "NotificationType", "Counter64", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ericsson = ModuleIdentity((1, 3, 6, 1, 4, 1, 193))
ericsson.setRevisions(('2008-10-17 00:00', '2002-05-28 00:00',))
if mibBuilder.loadTexts: ericsson.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericsson.setOrganization('Ericsson AB ')
ericssonModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 183))
if mibBuilder.loadTexts: ericssonModules.setStatus('current')
mibBuilder.exportSymbols("ERICSSON-TOP-MIB", PYSNMP_MODULE_ID=ericsson, ericssonModules=ericssonModules, ericsson=ericsson)
