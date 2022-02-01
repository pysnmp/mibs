#
# PySNMP MIB module ADTRAN-AOS-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.1.8 at Tue Feb  1 20:56:45 2022
# On host fv-az121-510 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
adGenAOSSwitch, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, MibIdentifier, Counter64, ModuleIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-AOS-PORT-SECURITY-MIB", adGenAOSPortSecurityTraps=adGenAOSPortSecurityTraps, PYSNMP_MODULE_ID=adGenAOSPortSecurityID, adGenAOSPortSecurityViolation=adGenAOSPortSecurityViolation, adGenAOSPortSecurity=adGenAOSPortSecurity, adGenAOSPortSecurityID=adGenAOSPortSecurityID)
