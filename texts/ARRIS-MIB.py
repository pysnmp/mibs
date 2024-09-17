#
# PySNMP MIB module ARRIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 11:59:39 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter64, TimeTicks, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, ObjectIdentity, Integer32, iso, Bits, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Integer32", "iso", "Bits", "enterprises", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
arris = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115))
arris.setRevisions(('1910-09-25 00:00', '1905-03-14 00:00', '1904-09-10 00:00', '1904-02-02 00:00', '1902-06-24 00:00', '1901-10-04 00:00', '1901-01-24 00:00', '1900-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arris.setRevisionsDescriptions(("Added Product Identifier 'arrisD5AM' for D5 Application Manager to the arrisProdIdVideo group", 'Updated Q5 naming to D5', "Added Product Group 'arrisProdIdVideo' for ARRIS video products.\n        Also added Product Identifier 'arrisQ5Wan' for Q5 WAN device.", "Added Product Identifier 'cmtsCommon' for common CMTS products.", "Added a ProductID OID for the 'tcm' product.       \n        Added the Global Access product line rooted at arrisProdIdGlobalAccess.", "Added a Product Identifier OID for the CM (Cable Modem) product line.\n        Added Product Identifier OIDs for the 'ttm' and 'ttp' products.", 'Added a Product Identifier OID for the MRC (Modular Redundant Chassis) product line.\n         Added a Product Identifier OID for the MRC Controller', 'Added a Product Identifier OID for the CMTS product line.\n\t     Added a Product Identifier OID for the MSAS (MultiService Access System) CMTS product.',))
if mibBuilder.loadTexts: arris.setLastUpdated('1009250000Z')
if mibBuilder.loadTexts: arris.setOrganization('Arris Interactive')
if mibBuilder.loadTexts: arris.setContactInfo('Robert Coley\n         Postal: Arris Interactive\n                 3871 Lakefield Drive\n                 Suite 300\n                 Suwanee, GA 30024-1242\n                 U.S.A.\n         Phone:  +1 770 622 8500\n         E-mail: robert.coley@arrisi.com\n   \n         Initial MIB creator: Angela Lyda\n         Postal: Arris Interactive\n                  3871 Lakefield Drive\n                  Suite 300\n                  Suwanee, GA 30024-1242\n                  U.S.A.\n          Phone:  +1 770 622 8743\n          E-mail: angela.lyda@arrisi.com')
if mibBuilder.loadTexts: arris.setDescription('This is a header for the Arris enterprise MIB.  All objects appear\n         elsewhere.')
arrisProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1))
packetport = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 1))
cm110 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 2))
arrisProdIdCM = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3))
arrisProdIdCMTS = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4))
arrisProdIdMRC = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 5))
arrisProdIdGlobalAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 6))
arrisProdIdVideo = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 8))
tcm = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 8))
ttm = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 9))
ttp = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 10))
cmtsMSAS = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 1))
cmts1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 2))
cmtsC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3))
cmtsC4 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 4))
cmtsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5))
mrcController = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 5, 1))
arrisGlobalAccessMib = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 6, 1))
arrisGlobalAccessProductUas = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 6, 2))
arrisD5UEQam = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 8, 1))
arrisD5AM = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 8, 2))
mibBuilder.exportSymbols("ARRIS-MIB", cmtsC4=cmtsC4, arrisGlobalAccessMib=arrisGlobalAccessMib, arrisProdIdVideo=arrisProdIdVideo, mrcController=mrcController, PYSNMP_MODULE_ID=arris, cmtsMSAS=cmtsMSAS, arrisD5UEQam=arrisD5UEQam, ttm=ttm, arrisProdIdGlobalAccess=arrisProdIdGlobalAccess, cmtsCommon=cmtsCommon, packetport=packetport, arrisProdIdCMTS=arrisProdIdCMTS, cm110=cm110, arrisD5AM=arrisD5AM, cmts1500=cmts1500, arrisProdIdCM=arrisProdIdCM, cmtsC3=cmtsC3, ttp=ttp, arrisProdIdMRC=arrisProdIdMRC, arris=arris, arrisProducts=arrisProducts, arrisGlobalAccessProductUas=arrisGlobalAccessProductUas, tcm=tcm)
