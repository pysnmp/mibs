#
# PySNMP MIB module ADTRAN-AOS-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 10:53:05 2024
# On host fv-az1986-135 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adGenAOSSwitch, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Bits, Counter32, Integer32, TimeTicks, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Bits", "Counter32", "Integer32", "TimeTicks", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSPortSecurityID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1))
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setLastUpdated('200410150000Z')
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setContactInfo('Technical Support Dept.\n                 Postal: ADTRAN, Inc.\n                         901 Explorer Blvd.\n                         Huntsville, AL 35806\n\n                         Tel: +1 800 726-8663\n                         Fax: +1 256 963 6217\n                         E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setDescription('The MIB module for general configuration of port security.')
adGenAOSPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1))
adGenAOSPortSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0))
adGenAOSPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0, 0)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOSPortSecurityViolation.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPortSecurityViolation.setDescription('This trap indicates a port security violation has occurred.')
mibBuilder.exportSymbols("ADTRAN-AOS-PORT-SECURITY-MIB", adGenAOSPortSecurity=adGenAOSPortSecurity, PYSNMP_MODULE_ID=adGenAOSPortSecurityID, adGenAOSPortSecurityViolation=adGenAOSPortSecurityViolation, adGenAOSPortSecurityID=adGenAOSPortSecurityID, adGenAOSPortSecurityTraps=adGenAOSPortSecurityTraps)
