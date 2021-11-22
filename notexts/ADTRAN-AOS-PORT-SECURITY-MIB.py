#
# PySNMP MIB module ADTRAN-AOS-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 20:01:37 2021
# On host fv-az42-715 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
adGenAOSSwitch, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, Integer32, Counter64, Gauge32, IpAddress, Counter32, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "Gauge32", "IpAddress", "Counter32", "iso", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSPortSecurityID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1))
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setLastUpdated('200410150000Z')
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setOrganization('ADTRAN, Inc.')
adGenAOSPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1))
adGenAOSPortSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0))
adGenAOSPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0, 0)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOSPortSecurityViolation.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-PORT-SECURITY-MIB", adGenAOSPortSecurityID=adGenAOSPortSecurityID, PYSNMP_MODULE_ID=adGenAOSPortSecurityID, adGenAOSPortSecurityTraps=adGenAOSPortSecurityTraps, adGenAOSPortSecurity=adGenAOSPortSecurity, adGenAOSPortSecurityViolation=adGenAOSPortSecurityViolation)
