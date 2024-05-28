#
# PySNMP MIB module ERICSSON-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TOP-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:08:31 2024
# On host fv-az1789-536 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, MibIdentifier, NotificationType, TimeTicks, Bits, ObjectIdentity, Unsigned32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "MibIdentifier", "NotificationType", "TimeTicks", "Bits", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ericsson = ModuleIdentity((1, 3, 6, 1, 4, 1, 193))
ericsson.setRevisions(('2008-10-17 00:00', '2002-05-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericsson.setRevisionsDescriptions(('Added email contact address, ericssonModules', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericsson.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericsson.setOrganization('Ericsson AB ')
if mibBuilder.loadTexts: ericsson.setContactInfo('Email: <snmp.mib.contact@ericsson.com>')
if mibBuilder.loadTexts: ericsson.setDescription("This very small module is made available so that\r\n        developers within the Ericsson community can import the\r\n        'ericsson' name into their own MIB modules.  In addition,\r\n        it includes the top-level node for Ericsson Group-wide\r\n        MIB modules.\r\n        \r\n        Document number: 1/196 03-CXC 172 7549, Rev A")
ericssonModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 183))
if mibBuilder.loadTexts: ericssonModules.setStatus('current')
if mibBuilder.loadTexts: ericssonModules.setDescription('ericssonModules provides a root object identifier\r\n        from which MODULE-IDENTITY values may be assigned\r\n        for Ericsson Group-wide MIB modules.')
mibBuilder.exportSymbols("ERICSSON-TOP-MIB", ericsson=ericsson, PYSNMP_MODULE_ID=ericsson, ericssonModules=ericssonModules)
