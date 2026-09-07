#
# PySNMP MIB module ALCATEL-IND1-OSPF3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALCATEL-IND1-OSPF3-MIB
# Source digest sha256:dce9e288f7b581b4e29b181c8222e61798ff223b3b789a1d5f2de32eba856b8b
# Produced by pysmi-2.3.0
#
routingIND1Ospf3, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ospf3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1OSPF3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1))
alcatelIND1OSPF3MIB.setRevisions(('2019-10-07 00:00',))
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setLastUpdated('2019-10-07 00:00')
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setOrganization('ALE USA Inc')
alcatelIND1OSPF3MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1))
alaProtocolOspf3 = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1))
alaOspf3OrigRouteTag = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 1), Unsigned32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3OrigRouteTag.setStatus('current')
alaOspf3TimerSpfDelay = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3TimerSpfDelay.setStatus('current')
alaOspf3TimerSpfHold = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3TimerSpfHold.setStatus('current')
alaOspf3RestartHelperSupport = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartHelperSupport.setStatus('current')
alaOspf3RestartStrictLsaChecking = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartStrictLsaChecking.setStatus('current')
alaOspf3RestartInitiate = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartInitiate.setStatus('current')
alaOspf3MTUCheck = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3MTUCheck.setStatus('current')
alcatelIND1OSPF3MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2))
alcatelIND1OSPF3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 1))
alcatelIND1OSPF3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 2))
alcatelIND1OSPF3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOSPF3ConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1OSPF3MIBCompliance = alcatelIND1OSPF3MIBCompliance.setStatus('current')
alaOSPF3ConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3OrigRouteTag"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfDelay"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfHold"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartHelperSupport"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartStrictLsaChecking"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartInitiate"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3MTUCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOSPF3ConfigMIBGroup = alaOSPF3ConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-OSPF3-MIB", PYSNMP_MODULE_ID=alcatelIND1OSPF3MIB, alaOSPF3ConfigMIBGroup=alaOSPF3ConfigMIBGroup, alaOspf3MTUCheck=alaOspf3MTUCheck, alaOspf3OrigRouteTag=alaOspf3OrigRouteTag, alaOspf3RestartHelperSupport=alaOspf3RestartHelperSupport, alaOspf3RestartInitiate=alaOspf3RestartInitiate, alaOspf3RestartStrictLsaChecking=alaOspf3RestartStrictLsaChecking, alaOspf3TimerSpfDelay=alaOspf3TimerSpfDelay, alaOspf3TimerSpfHold=alaOspf3TimerSpfHold, alaProtocolOspf3=alaProtocolOspf3, alcatelIND1OSPF3MIB=alcatelIND1OSPF3MIB, alcatelIND1OSPF3MIBCompliance=alcatelIND1OSPF3MIBCompliance, alcatelIND1OSPF3MIBCompliances=alcatelIND1OSPF3MIBCompliances, alcatelIND1OSPF3MIBConformance=alcatelIND1OSPF3MIBConformance, alcatelIND1OSPF3MIBGroups=alcatelIND1OSPF3MIBGroups, alcatelIND1OSPF3MIBObjects=alcatelIND1OSPF3MIBObjects)
