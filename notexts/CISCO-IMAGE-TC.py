#
# PySNMP MIB module CISCO-IMAGE-TC (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IMAGE-TC
# Source digest sha256:d1b6cc2f06e2217bbd61de642dfc30f4a5261104f6bfc05d790ba65c3facc464
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 455))
ciscoImageTc.setRevisions(('2005-01-12 00:00',))
if mibBuilder.loadTexts: ciscoImageTc.setLastUpdated('2005-01-12 00:00')
if mibBuilder.loadTexts: ciscoImageTc.setOrganization('Cisco Systems, Inc.')
class CeImageInstallableStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("active", 1), ("pendingInstall", 2), ("pendingRemoval", 3), ("installPendingReload", 4), ("removedPendingReload", 5), ("installPendingReloadPendingRemoval", 6), ("removedPendingReloadPendingInstall", 7), ("pruned", 8), ("inactive", 9))

class CeImageInstallableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("base", 1), ("patch", 2), ("script", 3), ("package", 4), ("compositePackage", 5), ("softwareMaintenanceUpgrade", 6))

mibBuilder.exportSymbols("CISCO-IMAGE-TC", CeImageInstallableStatus=CeImageInstallableStatus, CeImageInstallableType=CeImageInstallableType, PYSNMP_MODULE_ID=ciscoImageTc, ciscoImageTc=ciscoImageTc)
