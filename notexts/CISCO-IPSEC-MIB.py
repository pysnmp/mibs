#
# PySNMP MIB module CISCO-IPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPSEC-MIB
# Source digest sha256:1c5bbe8144d06417c1deb761c703b615ca6bd7ec80f3d459dd007b9302023e69
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoIPsecMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 62))
if mibBuilder.loadTexts: ciscoIPsecMIB.setLastUpdated('2000-08-07 11:39')
if mibBuilder.loadTexts: ciscoIPsecMIB.setOrganization('Cisco Systems, Inc.')
class CIPsecLifetime(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(120, 86400)

class CIPsecLifesize(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(2560, 536870912)

class CIPsecNumCryptoMaps(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CryptomapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("cryptomapTypeNONE", 0), ("cryptomapTypeMANUAL", 1), ("cryptomapTypeISAKMP", 2), ("cryptomapTypeCET", 3), ("cryptomapTypeDYNAMIC", 4), ("cryptomapTypeDYNAMICDISCOVERY", 5))

class CryptomapSetBindStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("attached", 1), ("detached", 2))

class IPSIpAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class IkeHashAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("md5", 2), ("sha", 3))

class IkeAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("preSharedKey", 2), ("rsaSig", 3), ("rsaEncrypt", 4), ("revPublicKey", 5))

class IkeIdentityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("isakmpIdTypeUNKNOWN", 0), ("isakmpIdTypeADDRESS", 1), ("isakmpIdTypeHOSTNAME", 2))

class DiffHellmanGrp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("dhGroup1", 2), ("dhGroup2", 3))

class EncryptAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("des", 2), ("des3", 3))

class TrapStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

ciscoIPsecMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1))
ciscoIPsecMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 2))
ciscoIPsecMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 3))
cipsIsakmpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1))
cipsIPsecGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2))
cipsIPsecGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1))
cipsIPsecStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2))
cipsCryptomapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3))
cipsSysCapacityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 3))
cipsTrapCntlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4))
cipsIsakmpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpEnabled.setStatus('current')
cipsIsakmpIdentity = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 2), IkeIdentityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpIdentity.setStatus('current')
cipsIsakmpKeepaliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpKeepaliveInterval.setStatus('current')
cipsNumIsakmpPolicies = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumIsakmpPolicies.setStatus('current')
cipsIsakmpPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsIsakmpPolicyTable.setStatus('current')
cipsIsakmpPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IPSEC-MIB", "cipsIsakmpPolPriority"))
if mibBuilder.loadTexts: cipsIsakmpPolicyEntry.setStatus('current')
cipsIsakmpPolPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsIsakmpPolPriority.setStatus('current')
cipsIsakmpPolEncr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 2), EncryptAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpPolEncr.setStatus('current')
cipsIsakmpPolHash = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 3), IkeHashAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpPolHash.setStatus('current')
cipsIsakmpPolAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 4), IkeAuthMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpPolAuth.setStatus('current')
cipsIsakmpPolGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 5), DiffHellmanGrp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpPolGroup.setStatus('current')
cipsIsakmpPolLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsIsakmpPolLifetime.setStatus('current')
cipsSALifetime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 1), CIPsecLifetime()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsSALifetime.setStatus('current')
cipsSALifesize = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 2), CIPsecLifesize()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsSALifesize.setStatus('current')
cipsNumStaticCryptomapSets = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 3), CIPsecNumCryptoMaps()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumStaticCryptomapSets.setStatus('current')
cipsNumCETCryptomapSets = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 4), CIPsecNumCryptoMaps()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumCETCryptomapSets.setStatus('current')
cipsNumDynamicCryptomapSets = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 5), CIPsecNumCryptoMaps()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumDynamicCryptomapSets.setStatus('current')
cipsNumTEDCryptomapSets = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 6), CIPsecNumCryptoMaps()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumTEDCryptomapSets.setStatus('current')
cipsNumTEDProbesReceived = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2, 1), Counter32()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumTEDProbesReceived.setStatus('current')
cipsNumTEDProbesSent = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2, 2), Counter32()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumTEDProbesSent.setStatus('current')
cipsNumTEDFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2, 3), Counter32()).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsNumTEDFailures.setStatus('current')
cipsMaxSAs = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('Integral Units').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsMaxSAs.setStatus('current')
cips3DesCapable = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 3, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cips3DesCapable.setStatus('current')
cipsStaticCryptomapSetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsStaticCryptomapSetTable.setStatus('current')
cipsStaticCryptomapSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapSetName"))
if mibBuilder.loadTexts: cipsStaticCryptomapSetEntry.setStatus('current')
cipsStaticCryptomapSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 1), DisplayString()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsStaticCryptomapSetName.setStatus('current')
cipsStaticCryptomapSetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetSize.setStatus('current')
cipsStaticCryptomapSetNumIsakmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetNumIsakmp.setStatus('current')
cipsStaticCryptomapSetNumManual = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetNumManual.setStatus('current')
cipsStaticCryptomapSetNumCET = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetNumCET.setStatus('current')
cipsStaticCryptomapSetNumDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetNumDynamic.setStatus('current')
cipsStaticCryptomapSetNumDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetNumDisc.setStatus('current')
cipsStaticCryptomapSetNumSAs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapSetNumSAs.setStatus('current')
cipsDynamicCryptomapSetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsDynamicCryptomapSetTable.setStatus('current')
cipsDynamicCryptomapSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IPSEC-MIB", "cipsDynamicCryptomapSetName"))
if mibBuilder.loadTexts: cipsDynamicCryptomapSetEntry.setStatus('current')
cipsDynamicCryptomapSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1, 1), DisplayString()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsDynamicCryptomapSetName.setStatus('current')
cipsDynamicCryptomapSetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsDynamicCryptomapSetSize.setStatus('current')
cipsDynamicCryptomapSetNumAssoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsDynamicCryptomapSetNumAssoc.setStatus('current')
cipsStaticCryptomapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsStaticCryptomapTable.setStatus('current')
cipsStaticCryptomapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapSetName"), (0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapPriority"))
if mibBuilder.loadTexts: cipsStaticCryptomapEntry.setStatus('current')
cipsStaticCryptomapPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsStaticCryptomapPriority.setStatus('current')
cipsStaticCryptomapType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 2), CryptomapType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapType.setStatus('current')
cipsStaticCryptomapDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapDescr.setStatus('current')
cipsStaticCryptomapPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 4), IPSIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapPeer.setStatus('current')
cipsStaticCryptomapNumPeers = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapNumPeers.setStatus('current')
cipsStaticCryptomapPfs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 6), DiffHellmanGrp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapPfs.setStatus('current')
cipsStaticCryptomapLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(120, 86400), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapLifetime.setStatus('current')
cipsStaticCryptomapLifesize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2560, 536870912), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapLifesize.setStatus('current')
cipsStaticCryptomapLevelHost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsStaticCryptomapLevelHost.setStatus('current')
cipsCryptomapSetIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cipsCryptomapSetIfTable.setStatus('current')
cipsCryptomapSetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapSetName"))
if mibBuilder.loadTexts: cipsCryptomapSetIfEntry.setStatus('current')
cipsCryptomapSetIfVirtual = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipsCryptomapSetIfVirtual.setStatus('current')
cipsCryptomapSetIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4, 1, 2), CryptomapSetBindStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCryptomapSetIfStatus.setStatus('current')
cipsCntlIsakmpPolicyAdded = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 1), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlIsakmpPolicyAdded.setStatus('current')
cipsCntlIsakmpPolicyDeleted = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 2), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlIsakmpPolicyDeleted.setStatus('current')
cipsCntlCryptomapAdded = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 3), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlCryptomapAdded.setStatus('current')
cipsCntlCryptomapDeleted = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 4), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlCryptomapDeleted.setStatus('current')
cipsCntlCryptomapSetAttached = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 5), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlCryptomapSetAttached.setStatus('current')
cipsCntlCryptomapSetDetached = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 6), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlCryptomapSetDetached.setStatus('current')
cipsCntlTooManySAs = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 7), TrapStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipsCntlTooManySAs.setStatus('current')
cipsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0))
cipsIsakmpPolicyAdded = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 1)).setObjects(("CISCO-IPSEC-MIB", "cipsNumIsakmpPolicies"))
if mibBuilder.loadTexts: cipsIsakmpPolicyAdded.setStatus('current')
cipsIsakmpPolicyDeleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 2)).setObjects(("CISCO-IPSEC-MIB", "cipsNumIsakmpPolicies"))
if mibBuilder.loadTexts: cipsIsakmpPolicyDeleted.setStatus('current')
cipsCryptomapAdded = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 3)).setObjects(("CISCO-IPSEC-MIB", "cipsStaticCryptomapType"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"))
if mibBuilder.loadTexts: cipsCryptomapAdded.setStatus('current')
cipsCryptomapDeleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 4)).setObjects(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"))
if mibBuilder.loadTexts: cipsCryptomapDeleted.setStatus('current')
cipsCryptomapSetAttached = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 5)).setObjects(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumIsakmp"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumDynamic"))
if mibBuilder.loadTexts: cipsCryptomapSetAttached.setStatus('current')
cipsCryptomapSetDetached = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 6)).setObjects(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"))
if mibBuilder.loadTexts: cipsCryptomapSetDetached.setStatus('current')
cipsTooManySAs = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 7)).setObjects(("CISCO-IPSEC-MIB", "cipsMaxSAs"))
if mibBuilder.loadTexts: cipsTooManySAs.setStatus('current')
cipsMIBConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 1))
cipsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2))
cipsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 1, 1)).setObjects(("CISCO-IPSEC-MIB", "cipsMIBConfIsakmpGroup"), ("CISCO-IPSEC-MIB", "cipsMIBConfIPSecGlobalsGroup"), ("CISCO-IPSEC-MIB", "cipsMIBConfCapacityGroup"), ("CISCO-IPSEC-MIB", "cipsMIBStaticCryptomapGroup"), ("CISCO-IPSEC-MIB", "cipsMIBMandatoryNotifCntlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBCompliance = cipsMIBCompliance.setStatus('current')
cipsMIBConfIsakmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 1)).setObjects(("CISCO-IPSEC-MIB", "cipsIsakmpEnabled"), ("CISCO-IPSEC-MIB", "cipsIsakmpIdentity"), ("CISCO-IPSEC-MIB", "cipsIsakmpKeepaliveInterval"), ("CISCO-IPSEC-MIB", "cipsNumIsakmpPolicies"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBConfIsakmpGroup = cipsMIBConfIsakmpGroup.setStatus('current')
cipsMIBConfIPSecGlobalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 2)).setObjects(("CISCO-IPSEC-MIB", "cipsSALifetime"), ("CISCO-IPSEC-MIB", "cipsSALifesize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBConfIPSecGlobalsGroup = cipsMIBConfIPSecGlobalsGroup.setStatus('current')
cipsMIBConfCapacityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 3)).setObjects(("CISCO-IPSEC-MIB", "cipsMaxSAs"), ("CISCO-IPSEC-MIB", "cips3DesCapable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBConfCapacityGroup = cipsMIBConfCapacityGroup.setStatus('current')
cipsMIBStaticCryptomapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 4)).setObjects(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumIsakmp"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumCET"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumSAs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBStaticCryptomapGroup = cipsMIBStaticCryptomapGroup.setStatus('current')
cipsMIBManualCryptomapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 5)).setObjects(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumManual"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBManualCryptomapGroup = cipsMIBManualCryptomapGroup.setStatus('current')
cipsMIBDynamicCryptomapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 6)).setObjects(("CISCO-IPSEC-MIB", "cipsNumTEDProbesReceived"), ("CISCO-IPSEC-MIB", "cipsNumTEDProbesSent"), ("CISCO-IPSEC-MIB", "cipsNumTEDFailures"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumDynamic"), ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumDisc"), ("CISCO-IPSEC-MIB", "cipsNumTEDCryptomapSets"), ("CISCO-IPSEC-MIB", "cipsDynamicCryptomapSetSize"), ("CISCO-IPSEC-MIB", "cipsDynamicCryptomapSetNumAssoc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBDynamicCryptomapGroup = cipsMIBDynamicCryptomapGroup.setStatus('current')
cipsMIBMandatoryNotifCntlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 7)).setObjects(("CISCO-IPSEC-MIB", "cipsCntlIsakmpPolicyAdded"), ("CISCO-IPSEC-MIB", "cipsCntlIsakmpPolicyDeleted"), ("CISCO-IPSEC-MIB", "cipsCntlCryptomapAdded"), ("CISCO-IPSEC-MIB", "cipsCntlCryptomapDeleted"), ("CISCO-IPSEC-MIB", "cipsCntlCryptomapSetAttached"), ("CISCO-IPSEC-MIB", "cipsCntlCryptomapSetDetached"), ("CISCO-IPSEC-MIB", "cipsCntlTooManySAs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cipsMIBMandatoryNotifCntlGroup = cipsMIBMandatoryNotifCntlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSEC-MIB", CIPsecLifesize=CIPsecLifesize, CIPsecLifetime=CIPsecLifetime, CIPsecNumCryptoMaps=CIPsecNumCryptoMaps, CryptomapSetBindStatus=CryptomapSetBindStatus, CryptomapType=CryptomapType, DiffHellmanGrp=DiffHellmanGrp, EncryptAlgo=EncryptAlgo, IPSIpAddress=IPSIpAddress, IkeAuthMethod=IkeAuthMethod, IkeHashAlgo=IkeHashAlgo, IkeIdentityType=IkeIdentityType, PYSNMP_MODULE_ID=ciscoIPsecMIB, TrapStatus=TrapStatus, cips3DesCapable=cips3DesCapable, cipsCntlCryptomapAdded=cipsCntlCryptomapAdded, cipsCntlCryptomapDeleted=cipsCntlCryptomapDeleted, cipsCntlCryptomapSetAttached=cipsCntlCryptomapSetAttached, cipsCntlCryptomapSetDetached=cipsCntlCryptomapSetDetached, cipsCntlIsakmpPolicyAdded=cipsCntlIsakmpPolicyAdded, cipsCntlIsakmpPolicyDeleted=cipsCntlIsakmpPolicyDeleted, cipsCntlTooManySAs=cipsCntlTooManySAs, cipsCryptomapAdded=cipsCryptomapAdded, cipsCryptomapDeleted=cipsCryptomapDeleted, cipsCryptomapGroup=cipsCryptomapGroup, cipsCryptomapSetAttached=cipsCryptomapSetAttached, cipsCryptomapSetDetached=cipsCryptomapSetDetached, cipsCryptomapSetIfEntry=cipsCryptomapSetIfEntry, cipsCryptomapSetIfStatus=cipsCryptomapSetIfStatus, cipsCryptomapSetIfTable=cipsCryptomapSetIfTable, cipsCryptomapSetIfVirtual=cipsCryptomapSetIfVirtual, cipsDynamicCryptomapSetEntry=cipsDynamicCryptomapSetEntry, cipsDynamicCryptomapSetName=cipsDynamicCryptomapSetName, cipsDynamicCryptomapSetNumAssoc=cipsDynamicCryptomapSetNumAssoc, cipsDynamicCryptomapSetSize=cipsDynamicCryptomapSetSize, cipsDynamicCryptomapSetTable=cipsDynamicCryptomapSetTable, cipsIPsecGlobals=cipsIPsecGlobals, cipsIPsecGroup=cipsIPsecGroup, cipsIPsecStatistics=cipsIPsecStatistics, cipsIsakmpEnabled=cipsIsakmpEnabled, cipsIsakmpGroup=cipsIsakmpGroup, cipsIsakmpIdentity=cipsIsakmpIdentity, cipsIsakmpKeepaliveInterval=cipsIsakmpKeepaliveInterval, cipsIsakmpPolAuth=cipsIsakmpPolAuth, cipsIsakmpPolEncr=cipsIsakmpPolEncr, cipsIsakmpPolGroup=cipsIsakmpPolGroup, cipsIsakmpPolHash=cipsIsakmpPolHash, cipsIsakmpPolLifetime=cipsIsakmpPolLifetime, cipsIsakmpPolPriority=cipsIsakmpPolPriority, cipsIsakmpPolicyAdded=cipsIsakmpPolicyAdded, cipsIsakmpPolicyDeleted=cipsIsakmpPolicyDeleted, cipsIsakmpPolicyEntry=cipsIsakmpPolicyEntry, cipsIsakmpPolicyTable=cipsIsakmpPolicyTable, cipsMIBCompliance=cipsMIBCompliance, cipsMIBConfCapacityGroup=cipsMIBConfCapacityGroup, cipsMIBConfIPSecGlobalsGroup=cipsMIBConfIPSecGlobalsGroup, cipsMIBConfIsakmpGroup=cipsMIBConfIsakmpGroup, cipsMIBConformances=cipsMIBConformances, cipsMIBDynamicCryptomapGroup=cipsMIBDynamicCryptomapGroup, cipsMIBGroups=cipsMIBGroups, cipsMIBMandatoryNotifCntlGroup=cipsMIBMandatoryNotifCntlGroup, cipsMIBManualCryptomapGroup=cipsMIBManualCryptomapGroup, cipsMIBNotifications=cipsMIBNotifications, cipsMIBStaticCryptomapGroup=cipsMIBStaticCryptomapGroup, cipsMaxSAs=cipsMaxSAs, cipsNumCETCryptomapSets=cipsNumCETCryptomapSets, cipsNumDynamicCryptomapSets=cipsNumDynamicCryptomapSets, cipsNumIsakmpPolicies=cipsNumIsakmpPolicies, cipsNumStaticCryptomapSets=cipsNumStaticCryptomapSets, cipsNumTEDCryptomapSets=cipsNumTEDCryptomapSets, cipsNumTEDFailures=cipsNumTEDFailures, cipsNumTEDProbesReceived=cipsNumTEDProbesReceived, cipsNumTEDProbesSent=cipsNumTEDProbesSent, cipsSALifesize=cipsSALifesize, cipsSALifetime=cipsSALifetime, cipsStaticCryptomapDescr=cipsStaticCryptomapDescr, cipsStaticCryptomapEntry=cipsStaticCryptomapEntry, cipsStaticCryptomapLevelHost=cipsStaticCryptomapLevelHost, cipsStaticCryptomapLifesize=cipsStaticCryptomapLifesize, cipsStaticCryptomapLifetime=cipsStaticCryptomapLifetime, cipsStaticCryptomapNumPeers=cipsStaticCryptomapNumPeers, cipsStaticCryptomapPeer=cipsStaticCryptomapPeer, cipsStaticCryptomapPfs=cipsStaticCryptomapPfs, cipsStaticCryptomapPriority=cipsStaticCryptomapPriority, cipsStaticCryptomapSetEntry=cipsStaticCryptomapSetEntry, cipsStaticCryptomapSetName=cipsStaticCryptomapSetName, cipsStaticCryptomapSetNumCET=cipsStaticCryptomapSetNumCET, cipsStaticCryptomapSetNumDisc=cipsStaticCryptomapSetNumDisc, cipsStaticCryptomapSetNumDynamic=cipsStaticCryptomapSetNumDynamic, cipsStaticCryptomapSetNumIsakmp=cipsStaticCryptomapSetNumIsakmp, cipsStaticCryptomapSetNumManual=cipsStaticCryptomapSetNumManual, cipsStaticCryptomapSetNumSAs=cipsStaticCryptomapSetNumSAs, cipsStaticCryptomapSetSize=cipsStaticCryptomapSetSize, cipsStaticCryptomapSetTable=cipsStaticCryptomapSetTable, cipsStaticCryptomapTable=cipsStaticCryptomapTable, cipsStaticCryptomapType=cipsStaticCryptomapType, cipsSysCapacityGroup=cipsSysCapacityGroup, cipsTooManySAs=cipsTooManySAs, cipsTrapCntlGroup=cipsTrapCntlGroup, ciscoIPsecMIB=ciscoIPsecMIB, ciscoIPsecMIBConformance=ciscoIPsecMIBConformance, ciscoIPsecMIBNotificationPrefix=ciscoIPsecMIBNotificationPrefix, ciscoIPsecMIBObjects=ciscoIPsecMIBObjects)
