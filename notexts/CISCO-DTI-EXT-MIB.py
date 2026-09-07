#
# PySNMP MIB module CISCO-DTI-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DTI-EXT-MIB
# Source digest sha256:32fdbea6c2b9aa50c3a5f3d20f63d751b3c31266482c86684701ef0fe42cf104
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dtiProtocolClientStatusFlag, dtiProtocolServerStatusFlag = mibBuilder.importSymbols("DTI-MIB", "dtiProtocolClientStatusFlag", "dtiProtocolServerStatusFlag")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoDtiExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 822))
ciscoDtiExtMIB.setRevisions(('2014-08-22 00:00',))
if mibBuilder.loadTexts: ciscoDtiExtMIB.setLastUpdated('2014-08-22 00:00')
if mibBuilder.loadTexts: ciscoDtiExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoDtiExtNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 0))
ciscoDtiExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 1))
ciscoDtiExtConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2))
cdeServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 1)).setObjects(("DTI-MIB", "dtiProtocolServerStatusFlag"))
if mibBuilder.loadTexts: cdeServerStatusChange.setStatus('current')
cdeClientStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 2)).setObjects(("DTI-MIB", "dtiProtocolClientStatusFlag"))
if mibBuilder.loadTexts: cdeClientStatusChange.setStatus('current')
ciscoDtiExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1))
cdeServerStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeServerStatusChangeEnable.setStatus('current')
cdeClientStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeClientStatusChangeEnable.setStatus('current')
ciscoDtiExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2))
ciscoDtiExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1, 1)).setObjects(("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsControlGroup"), ("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtCompliance = ciscoDtiExtCompliance.setStatus('current')
ciscoDtiExtNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 1)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChangeEnable"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChangeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsControlGroup = ciscoDtiExtNotifsControlGroup.setStatus('current')
ciscoDtiExtNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 2)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChange"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsGroup = ciscoDtiExtNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DTI-EXT-MIB", PYSNMP_MODULE_ID=ciscoDtiExtMIB, cdeClientStatusChange=cdeClientStatusChange, cdeClientStatusChangeEnable=cdeClientStatusChangeEnable, cdeServerStatusChange=cdeServerStatusChange, cdeServerStatusChangeEnable=cdeServerStatusChangeEnable, ciscoDtiExtCompliance=ciscoDtiExtCompliance, ciscoDtiExtCompliances=ciscoDtiExtCompliances, ciscoDtiExtConform=ciscoDtiExtConform, ciscoDtiExtGroups=ciscoDtiExtGroups, ciscoDtiExtMIB=ciscoDtiExtMIB, ciscoDtiExtNotifs=ciscoDtiExtNotifs, ciscoDtiExtNotifsControlGroup=ciscoDtiExtNotifsControlGroup, ciscoDtiExtNotifsGroup=ciscoDtiExtNotifsGroup, ciscoDtiExtObjects=ciscoDtiExtObjects)
