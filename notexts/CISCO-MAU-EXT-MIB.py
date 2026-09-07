#
# PySNMP MIB module CISCO-MAU-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MAU-EXT-MIB
# Source digest sha256:74e43e745b3b4fb4210d9dbdf01cfac268d027b0fbeaa83e42fd735696329505
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifJackEntry, ifMauIfIndex, ifMauIndex = mibBuilder.importSymbols("MAU-MIB", "ifJackEntry", "ifMauIfIndex", "ifMauIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoMauExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 398))
ciscoMauExtMIB.setRevisions(('2008-03-05 00:00', '2004-04-21 00:00',))
if mibBuilder.loadTexts: ciscoMauExtMIB.setLastUpdated('2008-03-05 00:00')
if mibBuilder.loadTexts: ciscoMauExtMIB.setOrganization('Cisco Systems, Inc.')
cmExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 0))
cmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1))
cmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2))
cmExtMauConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1))
cmExtJackConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmExtJackConfigTable.setStatus('current')
cmExtJackConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
ifJackEntry.registerAugmentions(("CISCO-MAU-EXT-MIB", "cmExtJackConfigEntry"))
cmExtJackConfigEntry.setIndexNames(*ifJackEntry.getIndexNames())
if mibBuilder.loadTexts: cmExtJackConfigEntry.setStatus('current')
cmExtJackState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmExtJackState.setStatus('current')
cmExtAutoMdixConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2))
cmExtIfAutoMdixConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmExtIfAutoMdixConfigTable.setStatus('current')
cmExtIfAutoMdixConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: cmExtIfAutoMdixConfigEntry.setStatus('current')
cmExtIfAutoMdixEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmExtIfAutoMdixEnabled.setStatus('current')
cmExtIfMau = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3))
cmExtIfMauTrafficTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmExtIfMauTrafficTable.setStatus('current')
cmExtIfMauTrafficEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: cmExtIfMauTrafficEntry.setStatus('current')
cmExtIfMauTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("adminControl", 2), ("user", 3))).clone('user')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmExtIfMauTrafficType.setStatus('current')
cmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1))
cmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2))
cmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 1)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance = cmExtMIBCompliance.setStatus('deprecated')
cmExtMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 2)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance2 = cmExtMIBCompliance2.setStatus('deprecated')
cmExtMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 3)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance3 = cmExtMIBCompliance3.setStatus('current')
cmExtJackConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 1)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtJackConfigGroup = cmExtJackConfigGroup.setStatus('current')
cmExtIfAutoMdixConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 2)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtIfAutoMdixConfigGroup = cmExtIfAutoMdixConfigGroup.setStatus('current')
cmExtIfMauTrafficGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 3)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtIfMauTrafficGroup = cmExtIfMauTrafficGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-EXT-MIB", PYSNMP_MODULE_ID=ciscoMauExtMIB, ciscoMauExtMIB=ciscoMauExtMIB, cmExtAutoMdixConfig=cmExtAutoMdixConfig, cmExtIfAutoMdixConfigEntry=cmExtIfAutoMdixConfigEntry, cmExtIfAutoMdixConfigGroup=cmExtIfAutoMdixConfigGroup, cmExtIfAutoMdixConfigTable=cmExtIfAutoMdixConfigTable, cmExtIfAutoMdixEnabled=cmExtIfAutoMdixEnabled, cmExtIfMau=cmExtIfMau, cmExtIfMauTrafficEntry=cmExtIfMauTrafficEntry, cmExtIfMauTrafficGroup=cmExtIfMauTrafficGroup, cmExtIfMauTrafficTable=cmExtIfMauTrafficTable, cmExtIfMauTrafficType=cmExtIfMauTrafficType, cmExtJackConfigEntry=cmExtJackConfigEntry, cmExtJackConfigGroup=cmExtJackConfigGroup, cmExtJackConfigTable=cmExtJackConfigTable, cmExtJackState=cmExtJackState, cmExtMIBCompliance2=cmExtMIBCompliance2, cmExtMIBCompliance3=cmExtMIBCompliance3, cmExtMIBCompliance=cmExtMIBCompliance, cmExtMIBCompliances=cmExtMIBCompliances, cmExtMIBConformance=cmExtMIBConformance, cmExtMIBGroups=cmExtMIBGroups, cmExtMIBNotifs=cmExtMIBNotifs, cmExtMIBObjects=cmExtMIBObjects, cmExtMauConfig=cmExtMauConfig)
