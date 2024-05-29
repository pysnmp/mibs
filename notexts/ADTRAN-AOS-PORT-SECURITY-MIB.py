#
# PySNMP MIB module ADTRAN-AOS-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:18:13 2024
# On host fv-az1984-402 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adGenAOSSwitch, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, IpAddress, MibIdentifier, ObjectIdentity, Integer32, Unsigned32, ModuleIdentity, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "Unsigned32", "ModuleIdentity", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSPortSecurityID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1))
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setLastUpdated('200410150000Z')
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setOrganization('ADTRAN, Inc.')
adGenAOSPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1))
adGenAOSPortSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0))
adGenAOSPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0, 0)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOSPortSecurityViolation.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-PORT-SECURITY-MIB", adGenAOSPortSecurityTraps=adGenAOSPortSecurityTraps, adGenAOSPortSecurityID=adGenAOSPortSecurityID, adGenAOSPortSecurityViolation=adGenAOSPortSecurityViolation, PYSNMP_MODULE_ID=adGenAOSPortSecurityID, adGenAOSPortSecurity=adGenAOSPortSecurity)
