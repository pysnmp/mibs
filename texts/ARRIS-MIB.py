#
# PySNMP MIB module ARRIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:04:11 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, IpAddress, Integer32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, MibIdentifier, Counter32, TimeTicks, iso, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "MibIdentifier", "Counter32", "TimeTicks", "iso", "enterprises", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ARRIS-MIB", arrisProdIdCM=arrisProdIdCM, cmtsC4=cmtsC4, ttm=ttm, arrisProdIdCMTS=arrisProdIdCMTS, arrisProdIdGlobalAccess=arrisProdIdGlobalAccess, mrcController=mrcController, cm110=cm110, arrisProdIdVideo=arrisProdIdVideo, cmtsMSAS=cmtsMSAS, arrisD5AM=arrisD5AM, arrisGlobalAccessMib=arrisGlobalAccessMib, cmtsCommon=cmtsCommon, arrisProdIdMRC=arrisProdIdMRC, arris=arris, cmts1500=cmts1500, arrisD5UEQam=arrisD5UEQam, PYSNMP_MODULE_ID=arris, packetport=packetport, arrisProducts=arrisProducts, tcm=tcm, arrisGlobalAccessProductUas=arrisGlobalAccessProductUas, ttp=ttp, cmtsC3=cmtsC3)
