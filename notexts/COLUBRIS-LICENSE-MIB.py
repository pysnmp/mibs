#
# PySNMP MIB module COLUBRIS-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-LICENSE-MIB.my
# Produced by pysmi-1.1.12 at Tue Sep 17 10:01:07 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, IpAddress, Counter32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, MibIdentifier, Bits, NotificationType, Counter64, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Counter32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "MibIdentifier", "Bits", "NotificationType", "Counter64", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 29))
if mibBuilder.loadTexts: colubrisLicenseMIB.setLastUpdated('200606070000Z')
if mibBuilder.loadTexts: colubrisLicenseMIB.setOrganization('Colubris Networks, Inc.')
colubrisLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1))
coLicenseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1))
coLicenseFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1), )
if mibBuilder.loadTexts: coLicenseFeatureTable.setStatus('current')
coLicenseFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-LICENSE-MIB", "coLicenseFeatureIndex"))
if mibBuilder.loadTexts: coLicenseFeatureEntry.setStatus('current')
coLicenseFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coLicenseFeatureIndex.setStatus('current')
coLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureName.setStatus('current')
coLicenseFeatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureState.setStatus('current')
coLicenseFeatureEndingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureEndingDate.setStatus('current')
coLicenseFeatureRemainingDays = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureRemainingDays.setStatus('current')
colubrisLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2))
colubrisLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 1))
colubrisLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 2))
colubrisLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 1, 1)).setObjects(("COLUBRIS-LICENSE-MIB", "colubrisLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisLicenseMIBCompliance = colubrisLicenseMIBCompliance.setStatus('current')
colubrisLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 2, 1)).setObjects(("COLUBRIS-LICENSE-MIB", "coLicenseFeatureName"), ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureState"), ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureEndingDate"), ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureRemainingDays"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisLicenseMIBGroup = colubrisLicenseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-LICENSE-MIB", coLicenseFeatureTable=coLicenseFeatureTable, coLicenseFeatureEntry=coLicenseFeatureEntry, colubrisLicenseMIBGroups=colubrisLicenseMIBGroups, coLicenseFeatureName=coLicenseFeatureName, colubrisLicenseMIBCompliance=colubrisLicenseMIBCompliance, colubrisLicenseMIBCompliances=colubrisLicenseMIBCompliances, colubrisLicenseMIBObjects=colubrisLicenseMIBObjects, PYSNMP_MODULE_ID=colubrisLicenseMIB, coLicenseFeatureEndingDate=coLicenseFeatureEndingDate, colubrisLicenseMIBConformance=colubrisLicenseMIBConformance, coLicenseFeatureState=coLicenseFeatureState, coLicenseFeatureRemainingDays=coLicenseFeatureRemainingDays, coLicenseGroup=coLicenseGroup, colubrisLicenseMIB=colubrisLicenseMIB, coLicenseFeatureIndex=coLicenseFeatureIndex, colubrisLicenseMIBGroup=colubrisLicenseMIBGroup)
