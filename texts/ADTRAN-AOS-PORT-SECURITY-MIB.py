#
# PySNMP MIB module ADTRAN-AOS-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:49:14 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSSwitch, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Bits, ModuleIdentity, Counter64, IpAddress, Integer32, Counter32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Bits", "ModuleIdentity", "Counter64", "IpAddress", "Integer32", "Counter32", "Unsigned32", "NotificationType")
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
mibBuilder.exportSymbols("ADTRAN-AOS-PORT-SECURITY-MIB", adGenAOSPortSecurityViolation=adGenAOSPortSecurityViolation, adGenAOSPortSecurity=adGenAOSPortSecurity, PYSNMP_MODULE_ID=adGenAOSPortSecurityID, adGenAOSPortSecurityTraps=adGenAOSPortSecurityTraps, adGenAOSPortSecurityID=adGenAOSPortSecurityID)
