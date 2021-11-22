#
# PySNMP MIB module UCD-DEMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/UCD-DEMO-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 11:34:50 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Integer32, Gauge32, Unsigned32, Counter64, iso, MibIdentifier, IpAddress, Bits, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32", "Counter64", "iso", "MibIdentifier", "IpAddress", "Bits", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
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
mibBuilder.exportSymbols("UCD-DEMO-MIB", ucdDemoPublic=ucdDemoPublic, ucdDemoPassphrase=ucdDemoPassphrase, ucdDemoUserList=ucdDemoUserList, ucdDemoMIBObjects=ucdDemoMIBObjects, ucdDemoResetKeys=ucdDemoResetKeys, ucdDemoMIB=ucdDemoMIB, ucdDemoPublicString=ucdDemoPublicString, PYSNMP_MODULE_ID=ucdDemoMIB)
