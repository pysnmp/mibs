#
# PySNMP MIB module ADTRAN-AOS-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 28 02:54:09 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
adGenAOSSwitch, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, ObjectIdentity, Integer32, NotificationType, MibIdentifier, iso, TimeTicks, Bits, IpAddress, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "iso", "TimeTicks", "Bits", "IpAddress", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSPortSecurityID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1))
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setLastUpdated('200410150000Z')
if mibBuilder.loadTexts: adGenAOSPortSecurityID.setOrganization('ADTRAN, Inc.')
adGenAOSPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1))
adGenAOSPortSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0))
adGenAOSPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0, 0)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOSPortSecurityViolation.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-PORT-SECURITY-MIB", adGenAOSPortSecurity=adGenAOSPortSecurity, adGenAOSPortSecurityViolation=adGenAOSPortSecurityViolation, adGenAOSPortSecurityTraps=adGenAOSPortSecurityTraps, PYSNMP_MODULE_ID=adGenAOSPortSecurityID, adGenAOSPortSecurityID=adGenAOSPortSecurityID)
