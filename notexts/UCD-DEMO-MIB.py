#
# PySNMP MIB module UCD-DEMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/UCD-DEMO-MIB
# Produced by pysmi-1.1.3 at Sat Nov 20 17:06:34 2021
# On host fv-az121-977 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, Counter64, Unsigned32, Bits, iso, Counter32, Gauge32, ObjectIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64", "Unsigned32", "Bits", "iso", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "NotificationType")
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
mibBuilder.exportSymbols("UCD-DEMO-MIB", ucdDemoPublic=ucdDemoPublic, PYSNMP_MODULE_ID=ucdDemoMIB, ucdDemoResetKeys=ucdDemoResetKeys, ucdDemoPassphrase=ucdDemoPassphrase, ucdDemoUserList=ucdDemoUserList, ucdDemoMIB=ucdDemoMIB, ucdDemoPublicString=ucdDemoPublicString, ucdDemoMIBObjects=ucdDemoMIBObjects)
