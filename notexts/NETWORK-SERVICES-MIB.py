#
# PySNMP MIB module NETWORK-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/NETWORK-SERVICES-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:04:40 2021
# On host fv-az36-755 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, Counter32, IpAddress, MibIdentifier, mib_2, Bits, TimeTicks, iso, Integer32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "MibIdentifier", "mib-2", "Bits", "TimeTicks", "iso", "Integer32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
application = ModuleIdentity((1, 3, 6, 1, 2, 1, 27))
application.setRevisions(('2000-03-03 00:00', '1999-05-12 00:00', '1997-08-17 00:00', '1993-11-28 00:00',))
if mibBuilder.loadTexts: application.setLastUpdated('200003030000Z')
if mibBuilder.loadTexts: application.setOrganization('IETF Mail and Directory Management Working Group')
class DistinguishedName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class URLString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

applTable = MibTable((1, 3, 6, 1, 2, 1, 27, 1), )
if mibBuilder.loadTexts: applTable.setStatus('current')
applEntry = MibTableRow((1, 3, 6, 1, 2, 1, 27, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: applEntry.setStatus('current')
applIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: applIndex.setStatus('current')
applName = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applName.setStatus('current')
applDirectoryName = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 3), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applDirectoryName.setStatus('current')
applVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applVersion.setStatus('current')
applUptime = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applUptime.setStatus('current')
applOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("halted", 3), ("congested", 4), ("restarting", 5), ("quiescing", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: applOperStatus.setStatus('current')
applLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastChange.setStatus('current')
applInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applInboundAssociations.setStatus('current')
applOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applOutboundAssociations.setStatus('current')
applAccumulatedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applAccumulatedInboundAssociations.setStatus('current')
applAccumulatedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applAccumulatedOutboundAssociations.setStatus('current')
applLastInboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastInboundActivity.setStatus('current')
applLastOutboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastOutboundActivity.setStatus('current')
applRejectedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applRejectedInboundAssociations.setStatus('current')
applFailedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applFailedOutboundAssociations.setStatus('current')
applDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applDescription.setStatus('current')
applURL = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 17), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applURL.setStatus('current')
assocTable = MibTable((1, 3, 6, 1, 2, 1, 27, 2), )
if mibBuilder.loadTexts: assocTable.setStatus('current')
assocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 27, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "NETWORK-SERVICES-MIB", "assocIndex"))
if mibBuilder.loadTexts: assocEntry.setStatus('current')
assocIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: assocIndex.setStatus('current')
assocRemoteApplication = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocRemoteApplication.setStatus('current')
assocApplicationProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocApplicationProtocol.setStatus('current')
assocApplicationType = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uainitiator", 1), ("uaresponder", 2), ("peerinitiator", 3), ("peerresponder", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocApplicationType.setStatus('current')
assocDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocDuration.setStatus('current')
applConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3))
applGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3, 1))
applCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3, 2))
applCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 1)).setObjects(("NETWORK-SERVICES-MIB", "applRFC1565Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applCompliance = applCompliance.setStatus('obsolete')
assocCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 2)).setObjects(("NETWORK-SERVICES-MIB", "applRFC1565Group"), ("NETWORK-SERVICES-MIB", "assocRFC1565Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocCompliance = assocCompliance.setStatus('obsolete')
applRFC2248Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 3)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2248Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2248Compliance = applRFC2248Compliance.setStatus('deprecated')
assocRFC2248Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 4)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2248Group"), ("NETWORK-SERVICES-MIB", "assocRFC2248Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2248Compliance = assocRFC2248Compliance.setStatus('deprecated')
applRFC2788Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 5)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2788Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2788Compliance = applRFC2788Compliance.setStatus('current')
assocRFC2788Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 6)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2788Group"), ("NETWORK-SERVICES-MIB", "assocRFC2788Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2788Compliance = assocRFC2788Compliance.setStatus('current')
applRFC1565Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 7)).setObjects(("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC1565Group = applRFC1565Group.setStatus('obsolete')
assocRFC1565Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 2)).setObjects(("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), ("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC1565Group = assocRFC1565Group.setStatus('obsolete')
applRFC2248Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 3)).setObjects(("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applDescription"), ("NETWORK-SERVICES-MIB", "applURL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2248Group = applRFC2248Group.setStatus('deprecated')
assocRFC2248Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 4)).setObjects(("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), ("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2248Group = assocRFC2248Group.setStatus('deprecated')
applRFC2788Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 5)).setObjects(("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applDirectoryName"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applDescription"), ("NETWORK-SERVICES-MIB", "applURL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2788Group = applRFC2788Group.setStatus('current')
assocRFC2788Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 6)).setObjects(("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), ("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2788Group = assocRFC2788Group.setStatus('current')
applTCPProtoID = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 4))
applUDPProtoID = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 5))
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", assocApplicationType=assocApplicationType, applRFC2248Compliance=applRFC2248Compliance, applIndex=applIndex, applRFC2248Group=applRFC2248Group, applUDPProtoID=applUDPProtoID, applRFC2788Group=applRFC2788Group, applLastChange=applLastChange, URLString=URLString, assocRFC2248Compliance=assocRFC2248Compliance, applAccumulatedOutboundAssociations=applAccumulatedOutboundAssociations, applGroups=applGroups, applURL=applURL, applOperStatus=applOperStatus, application=application, assocEntry=assocEntry, applOutboundAssociations=applOutboundAssociations, applDirectoryName=applDirectoryName, PYSNMP_MODULE_ID=application, DistinguishedName=DistinguishedName, applLastInboundActivity=applLastInboundActivity, applTCPProtoID=applTCPProtoID, applRFC2788Compliance=applRFC2788Compliance, assocRFC2788Compliance=assocRFC2788Compliance, assocCompliance=assocCompliance, assocRFC2788Group=assocRFC2788Group, applFailedOutboundAssociations=applFailedOutboundAssociations, applCompliance=applCompliance, applUptime=applUptime, applAccumulatedInboundAssociations=applAccumulatedInboundAssociations, assocRFC1565Group=assocRFC1565Group, applRejectedInboundAssociations=applRejectedInboundAssociations, applCompliances=applCompliances, assocRemoteApplication=assocRemoteApplication, applName=applName, assocIndex=assocIndex, assocDuration=assocDuration, applLastOutboundActivity=applLastOutboundActivity, applConformance=applConformance, applDescription=applDescription, assocTable=assocTable, applVersion=applVersion, applEntry=applEntry, assocRFC2248Group=assocRFC2248Group, applInboundAssociations=applInboundAssociations, applRFC1565Group=applRFC1565Group, applTable=applTable, assocApplicationProtocol=assocApplicationProtocol)
