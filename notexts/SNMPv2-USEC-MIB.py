#
# PySNMP MIB module SNMPv2-USEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SNMPv2-USEC-MIB
# Source digest sha256:ee483819157693860c813c695bf33fcb7c9e3978257deaae5fca4a5194d90098
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, snmpModules = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "snmpModules")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usecMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 6))
if mibBuilder.loadTexts: usecMIB.setLastUpdated('1996-01-12 00:00')
if mibBuilder.loadTexts: usecMIB.setOrganization('IETF SNMPv2 Working Group')
usecMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1))
class AgentID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

usecAgent = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1, 1))
agentID = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 1), AgentID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentID.setStatus('current')
agentBoots = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentBoots.setStatus('current')
agentTime = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentTime.setStatus('current')
agentSize = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 65507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSize.setStatus('current')
usecStats = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1, 2))
usecStatsUnsupportedQoS = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnsupportedQoS.setStatus('current')
usecStatsNotInWindows = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsNotInWindows.setStatus('current')
usecStatsUnknownUserNames = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnknownUserNames.setStatus('current')
usecStatsWrongDigestValues = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsWrongDigestValues.setStatus('current')
usecStatsUnknownContexts = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnknownContexts.setStatus('current')
usecStatsBadParameters = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsBadParameters.setStatus('current')
usecStatsUnauthorizedOperations = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnauthorizedOperations.setStatus('current')
usecMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2))
usecMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2, 1))
usecMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2, 2))
usecMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 6, 2, 1, 1)).setObjects(("SNMPv2-USEC-MIB", "usecBasicGroup"), ("SNMPv2-USEC-MIB", "usecStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecMIBCompliance = usecMIBCompliance.setStatus('current')
usecBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 6, 2, 2, 1)).setObjects(("SNMPv2-USEC-MIB", "agentID"), ("SNMPv2-USEC-MIB", "agentBoots"), ("SNMPv2-USEC-MIB", "agentTime"), ("SNMPv2-USEC-MIB", "agentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecBasicGroup = usecBasicGroup.setStatus('current')
usecStatsGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 6, 2, 2, 2)).setObjects(("SNMPv2-USEC-MIB", "usecStatsUnsupportedQoS"), ("SNMPv2-USEC-MIB", "usecStatsNotInWindows"), ("SNMPv2-USEC-MIB", "usecStatsUnknownUserNames"), ("SNMPv2-USEC-MIB", "usecStatsWrongDigestValues"), ("SNMPv2-USEC-MIB", "usecStatsUnknownContexts"), ("SNMPv2-USEC-MIB", "usecStatsBadParameters"), ("SNMPv2-USEC-MIB", "usecStatsUnauthorizedOperations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecStatsGroup = usecStatsGroup.setStatus('current')
mibBuilder.exportSymbols("SNMPv2-USEC-MIB", AgentID=AgentID, PYSNMP_MODULE_ID=usecMIB, agentBoots=agentBoots, agentID=agentID, agentSize=agentSize, agentTime=agentTime, usecAgent=usecAgent, usecBasicGroup=usecBasicGroup, usecMIB=usecMIB, usecMIBCompliance=usecMIBCompliance, usecMIBCompliances=usecMIBCompliances, usecMIBConformance=usecMIBConformance, usecMIBGroups=usecMIBGroups, usecMIBObjects=usecMIBObjects, usecStats=usecStats, usecStatsBadParameters=usecStatsBadParameters, usecStatsGroup=usecStatsGroup, usecStatsNotInWindows=usecStatsNotInWindows, usecStatsUnauthorizedOperations=usecStatsUnauthorizedOperations, usecStatsUnknownContexts=usecStatsUnknownContexts, usecStatsUnknownUserNames=usecStatsUnknownUserNames, usecStatsUnsupportedQoS=usecStatsUnsupportedQoS, usecStatsWrongDigestValues=usecStatsWrongDigestValues)
