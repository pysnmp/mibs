#
# PySNMP MIB module UCD-DEMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/UCD-DEMO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 15:20:13 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, TimeTicks, NotificationType, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, iso, MibIdentifier, IpAddress, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "iso", "MibIdentifier", "IpAddress", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucdavis, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdavis")
ucdDemoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 14))
ucdDemoMIB.setRevisions(('1999-12-09 00:00',))
if mibBuilder.loadTexts: ucdDemoMIB.setLastUpdated('9912090000Z')
if mibBuilder.loadTexts: ucdDemoMIB.setOrganization('University of California, Davis')
ucdDemoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 14, 1))
ucdDemoPublic = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1))
ucdDemoResetKeys = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ucdDemoResetKeys.setStatus('current')
ucdDemoPublicString = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ucdDemoPublicString.setStatus('current')
ucdDemoUserList = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ucdDemoUserList.setStatus('current')
ucdDemoPassphrase = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ucdDemoPassphrase.setStatus('current')
mibBuilder.exportSymbols("UCD-DEMO-MIB", PYSNMP_MODULE_ID=ucdDemoMIB, ucdDemoResetKeys=ucdDemoResetKeys, ucdDemoUserList=ucdDemoUserList, ucdDemoPassphrase=ucdDemoPassphrase, ucdDemoMIBObjects=ucdDemoMIBObjects, ucdDemoPublicString=ucdDemoPublicString, ucdDemoPublic=ucdDemoPublic, ucdDemoMIB=ucdDemoMIB)
