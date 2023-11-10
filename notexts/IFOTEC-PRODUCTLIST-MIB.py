#
# PySNMP MIB module IFOTEC-PRODUCTLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ifotec/IFOTEC-PRODUCTLIST-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:45:48 2023
# On host fv-az566-171 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ifotec, = mibBuilder.importSymbols("IFOTEC-SMI", "ifotec")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Unsigned32, ObjectIdentity, IpAddress, NotificationType, Gauge32, MibIdentifier, Counter32, Integer32, ModuleIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Unsigned32", "ObjectIdentity", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "Counter32", "Integer32", "ModuleIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("IFOTEC-PRODUCTLIST-MIB", INET_4GE2GF_KS_001=INET_4GE2GF_KS_001, INET_2GP2GF_AS_101=INET_2GP2GF_AS_101, ifotecEthernetProducts=ifotecEthernetProducts, INET_2GE2GF_AS_101=INET_2GE2GF_AS_101, ifotecProductList=ifotecProductList, INET_4GP2GF_AS_001=INET_4GP2GF_AS_001, INET_4GE2GF2XF_R1_001=INET_4GE2GF2XF_R1_001, ifotecL2ManagedSwitches=ifotecL2ManagedSwitches, PYSNMP_MODULE_ID=ifotecProductList, ifotecINETFamilly=ifotecINETFamilly)
