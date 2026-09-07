#
# PySNMP MIB module CISCO-ROUTE-POLICIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ROUTE-POLICIES-MIB
# Source digest sha256:201df3749da3f87ddb273a425cae6c4ebc09c6b06ebaad986a504539473eacf2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRoutePoliciesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578))
ciscoRoutePoliciesMIB.setRevisions(('2006-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setLastUpdated('2006-08-18 00:00')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setOrganization('Cisco Systems, Inc. ')
ciscoRoutePoliciesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 0))
ciscoRoutePoliciesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 1))
ciscoRoutePoliciesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 2))
crpPolicies = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1))
if mibBuilder.loadTexts: crpPolicies.setStatus('current')
crpPolicyIfIndex = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1, 1))
if mibBuilder.loadTexts: crpPolicyIfIndex.setStatus('current')
mibBuilder.exportSymbols("CISCO-ROUTE-POLICIES-MIB", PYSNMP_MODULE_ID=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIB=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIBConform=ciscoRoutePoliciesMIBConform, ciscoRoutePoliciesMIBNotifs=ciscoRoutePoliciesMIBNotifs, ciscoRoutePoliciesMIBObjects=ciscoRoutePoliciesMIBObjects, crpPolicies=crpPolicies, crpPolicyIfIndex=crpPolicyIfIndex)
