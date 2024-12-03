#
# PySNMP MIB module IFOTEC-PRODUCTLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ifotec/IFOTEC-PRODUCTLIST-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:08:24 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifotec, = mibBuilder.importSymbols("IFOTEC-SMI", "ifotec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, Counter32, iso, IpAddress, Gauge32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "Counter32", "iso", "IpAddress", "Gauge32", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ifotecProductList = ModuleIdentity((1, 3, 6, 1, 4, 1, 21362, 100))
if mibBuilder.loadTexts: ifotecProductList.setLastUpdated('202007290000Z')
if mibBuilder.loadTexts: ifotecProductList.setOrganization('IFOTEC')
ifotecEthernetProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1))
ifotecL2ManagedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4))
ifotecINETFamilly = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3))
INET_2GE2GF_AS_101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 1)).setLabel("INET-2GE2GF-AS-101")
INET_2GP2GF_AS_101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 2)).setLabel("INET-2GP2GF-AS-101")
INET_4GE2GF_KS_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 3)).setLabel("INET-4GE2GF-KS-001")
INET_4GP2GF_AS_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 4)).setLabel("INET-4GP2GF-AS-001")
INET_4GE2GF2XF_R1_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 5)).setLabel("INET-4GE2GF2XF-R1-001")
mibBuilder.exportSymbols("IFOTEC-PRODUCTLIST-MIB", INET_2GP2GF_AS_101=INET_2GP2GF_AS_101, PYSNMP_MODULE_ID=ifotecProductList, INET_2GE2GF_AS_101=INET_2GE2GF_AS_101, ifotecINETFamilly=ifotecINETFamilly, INET_4GE2GF_KS_001=INET_4GE2GF_KS_001, INET_4GE2GF2XF_R1_001=INET_4GE2GF2XF_R1_001, ifotecL2ManagedSwitches=ifotecL2ManagedSwitches, ifotecEthernetProducts=ifotecEthernetProducts, ifotecProductList=ifotecProductList, INET_4GP2GF_AS_001=INET_4GP2GF_AS_001)
